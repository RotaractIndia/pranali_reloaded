<template>
	<div>
		<div class="muted-title">{{ __('Upcoming Events') }}</div>
		<div class="event" v-for="event in events" :key="event.name">
			<span class="bold">{{ get_time(event.starts_on) }}</span>
			<a @click="open_event(event)"> {{ event.subject }}</a>
		</div>
		<div class="event" v-if="!events.length">
			{{ __('No Upcoming Events') }}
		</div>
		<div class="muted-title">{{ __('Upcoming Birthdays') }}</div>
		<div class="birthday" v-for="birthday in birthdays" :key="birthday.member_name">
			<span class="bold">{{ get_date(birthday.dob) }}</span>
		</div>
		<div class="birthday" v-if="!birthdays.length">
			{{ __('No Upcoming Birthdays') }}
		</div>
		<div class="muted-title">{{ __('Chat') }}</div>
		<a @click="open_chat">
			{{ __('Open Chat') }}
		</a>
	</div>
</template>
<script>
export default {
	data() {
		return {
			'events': [],
			'birthdays': []
		}
	},
	created() {
		this.get_events().then((events) => {
			this.events = events
		}),
		this.get_birthdays().then((birthdays) => {
			this.birthdays = birthdays
		})
	},
	methods: {
		get_events() {
			const today = frappe.datetime.now_date();
			return frappe.xcall('frappe.desk.doctype.event.event.get_events', {
				start: today,
				end: today
			})
		},
		get_birthdays() {
			const today = frappe.datetime.now_date();
			return frappe.xcall('pranali_reloaded.pranali_reloaded.api.get_birthdays', {
				start_date: today
			})
		},
		open_chat() {
			setTimeout(frappe.chat.widget.toggle);
		},
		get_time(timestamp) {
			return frappe.datetime.get_time(timestamp)
		},
		open_event(event) {
			frappe.set_route('Form', 'Event', event.name);
		}
	}
}
</script>
