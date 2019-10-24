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
	constructor(wrapper) {
		this.setup(wrapper);
		const assets = [
			'assets/js/chart.js',
			'assets/pranali_reloaded/css/insight_engine.css'
		];

		frappe.require(assets, () => {
			this.make();
		});
	}

	setup(wrapper) {
		let me = this;
		this.elements = {
			parent: $(wrapper).find(".layout-main"),
			refresh_btn: wrapper.page.set_primary_action(__("Refresh All"), () => { me.make() }, "fa fa-refresh"),
		};

		this.elements.no_data = $('<div class="alert alert-warning">' + __("No Data") + '</div>')
			.toggle(false)
			.appendTo(this.elements.parent);

		wrapper.page.add_field({
			fieldname: "club",
			label: __("Club"),
			fieldtype: "Link",
			options: "Club",
			reqd: 1,
			change: (field) => {
				me.elements.selected_club = field.currentTarget.value;
				me.make();
			}
		});
	}

	async make() {
		await this.getData();
		this.renderPage();
		this.renderCharts();
	}

	async getData() {
		let me = this;
		console.log(this)
		await frappe.call({
			method: "pranali_reloaded.pranali_reloaded.page.insight_engine.insight_engine.get_dashboards",
			args: {
				// "club": me.elements.selected_club || ""
				"club": " "
			},
			callback: (r) => {
				if (!r.exc && r.message) {
					me.dashboard_data = r.message;
				} else {
					me.elements.no_data.toggle(true);
				}
			}
		});
	}

	getDateRangeAsArray(startDate, stopDate) {
		let dateArray = [];

		// Default the dashboard input dates to a week
		startDate = moment(startDate || moment().subtract(7, 'days'));
		stopDate = moment(stopDate || moment().subtract(1, 'day'));

		while (startDate <= stopDate) {
			dateArray.push(moment(startDate).format('MMM D'))
			startDate = moment(startDate).add(1, 'day');
		}

		return dateArray;
	}

	renderPage() {
		let html = frappe.render_template("insight_engine", this.dashboard_data)
		this.elements.parent.html(html);
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
					callbacks: {
						label(tooltipItem, data) {
							return data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index];
						}
					}
				}
			}
		});

		// Most Profitable Projects
		this.dashboard_data.top_projects.map((data, i) => {
			let row = `
				<tr>
					<td> ${ (i+1) } </td>
					<td> ${ data.project_name } </td>
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
							callback(value, index, values) {
								return value;
							}
						}
					}]
				},
				tooltips: {
					callbacks: {
						label(tooltipItem, data) {
							return tooltipItem.value;
						}
					}
				}
			}
		});		
	}
}
