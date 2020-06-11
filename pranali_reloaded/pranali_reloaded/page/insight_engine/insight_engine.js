{% include "pranali_reloaded/pranali_reloaded/page/insight_engine/insight_engine.html" %}

frappe.pages['insight-engine'].on_page_load = function(wrapper) {
	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Insight Engine',
		single_column: true
	});

	wrapper.page = page;
	wrapper.insight_engine = new InsightEngine(wrapper);
}

InsightEngine = class InsightEngine {
	constructor(parent) {
		this.setup(parent);
		const assets = [
			'assets/js/chart.js',
			'assets/pranali_reloaded/css/insight_engine.css'
		];

		frappe.require(assets, () => {
			this.make();
		});
	}

	setup(parent) {
		let me = this;
		let club_control = parent.page.add_field({
			fieldname: "club",
			label: __("Club"),
			fieldtype: "Link",
			options: "Club",
			reqd: 1,
			change: (field) => {
				me.make();
			}
		});


		this.elements = {
			parent: $(parent).find(".layout-main"),
			club: club_control,
			refresh_btn: parent.page.set_primary_action(__("Refresh All"), () => { me.make() }, "fa fa-refresh"),
		};

		this.elements.no_data = $('<div class="alert alert-warning">' + __("No Data") + '</div>')
			.toggle(false)
			.appendTo(this.elements.parent);

	}

	async make() {
		await this.getData();
		this.renderPage();
		this.renderCharts();
	}

	async getData() {
		let me = this;
		await frappe.call({
			method: "pranali_reloaded.pranali_reloaded.page.insight_engine.insight_engine.get_dashboards",
			args: {
				"club": me.elements.club.value,
			},
			callback: (r) => {
				if (!r.exc && r.message) {
					me.elements.no_data.toggle(false);
					me.dashboard_data = r.message;
				} else {
					me.elements.no_data.toggle(true);
				}
			}
		});
	}

	renderPage() {
		let html = frappe.render_template("insight_engine", this.dashboard_data);
		let wrapper = this.elements.parent.find(".wrapper");

		if (wrapper.length) {
			wrapper.html(html);
		} else {
			this.elements.parent.append(html);
		}
	}

	renderCharts() {
		const opacity = 0.6;
		const colors = ['#eeef37','#ff6a05','#0c8d00','#21bda9', '#7bf2bf', 
			'#f0c789', '#704041', '#adf2f1', '#ef9798', '#f4b02f', '#009fff', '#197a64']

		// Reporting Status
		new Chart($(".category-product-info .donut-chart .graphics"), {
			type: 'doughnut',
			data: {
				labels: this.dashboard_data.reporting_status.map(elem => elem.status),
				datasets: [{
					data: this.dashboard_data.reporting_status.map(elem => elem.count),
					backgroundColor: colors,
					borderColor: colors,
					borderWidth: 1.5
				}]
			},
			options: {
				layout: { padding: 30 },
				legend: { position: 'left' },
				tooltips: {
					intersect : false,
					mode:'nearest'
				}
			}
		});

		// Most Profitable Projects
		this.dashboard_data.top_projects.map((data, i) => {
			var project_link = "/desk#Form/Project/" + data.name;
			let row = `
				<tr>
					<td> ${ (i+1) } </td>
					<td> <a href= ${ project_link } target= "_blank" > ${ data.project_name } </a></td>
					<td> ${ data.avenue_1 } </td>
					<td> ${ data.avenue_2 } </td>
					<td> ₹  ${ data.net_profit } </td>
				</tr>
			`;
			$('.table-data tbody').append(row);
		});

		// Avenue wise project count
		let datasets = [];
		Object.keys(this.dashboard_data.projects_per_month).forEach((item, i) => {
			if(i < 11) {
				datasets.push({
					label: item,
					backgroundColor: colors[i],
					borderColor: colors[i],
					borderWidth: 1.5,
					fill: false,
					data: this.dashboard_data.projects_per_month[item]
				})
			}
		});

		new Chart($(".chart-graphics"), {
			type: 'line',
			data: {
				labels: this.dashboard_data.reporting_months,
				datasets: datasets
			},
			options: {
				legend: { position: 'bottom' },
				layout: { padding: 30 },
				scales: {
					xAxes: [{
						gridLines: { display: false }
					}],
					yAxes: [{
						gridLines: { display: false },
						ticks: {
							stepSize: 1,
							callback(value, index, values) {
								return value;
							}
						}
					}]
				},
				tooltips: {
					tooltips: {
						intersect : false,
						mode:'nearest'
					}
				}
			}
		});	
		
		// Avenue wise time spent on projects
		let time_datasets = [];
		Object.keys(this.dashboard_data.projects_time_per_month).forEach((item, i) => {
			if(i < 11) {
				time_datasets.push({
					label: item,
					backgroundColor: colors[i],
					borderColor: colors[i],
					borderWidth: 1.5,
					fill: false,
					data: this.dashboard_data.projects_time_per_month[item]
				})
			}
		});

		new Chart($(".chart-time-graphics"), {
			type: 'line',
			data: {
				labels: this.dashboard_data.reporting_months,
				datasets: time_datasets
			},
			options: {
				legend: { position: 'bottom' },
				layout: { padding: 30 },
				scales: {
					xAxes: [{
						gridLines: { display: false }
					}],
					yAxes: [{
						gridLines: { display: false },
						ticks: {
							stepSize: 250,
							callback(value, index, values) {
								return value;
							}
						}
					}]
				},
				tooltips: {
					tooltips: {
						intersect : false,
						mode:'nearest'
					}
				}
			}
		});
	}
}