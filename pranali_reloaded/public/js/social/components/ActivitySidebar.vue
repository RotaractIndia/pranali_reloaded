<template>
  <div>
    <div class="heading">{{ __('Upcoming Events') }}</div>
    <div class="event" v-for="event in events" :key="event.name">
      <span class="bold">{{ get_time(event.starts_on) }}</span>
      <a @click="open_event(event)">{{ event.subject }}</a>
    </div>
    <div class="event" v-if="!events.length">{{ __('No Upcoming Events') }}</div>

    <div class="heading">{{ __('Birthdays') }}</div>
    <div class="muted-title-birthday">{{ __('Today') }}</div>

    <div class="birthday" v-for="TodBirthday in birthdays.today" :key="TodBirthday.member_name">
      <span class="birthday-value">{{TodBirthday.member_name}}, {{TodBirthday.club}}</span>
    </div>
    <div class="birthday" v-if="!birthdays.today">{{ __('No Birthdays Today') }}</div>

    <div class="muted-title-birthday">{{ __('Yesterday') }}</div>
    <div
      class="birthday"
      v-for="YestBirthday in birthdays.yesterday"
      :key="YestBirthday.member_name"
    >
      <span class="birthday-value">{{YestBirthday.member_name}}, {{YestBirthday.club}}</span>
    </div>
    <div class="birthday" v-if="!birthdays.yesterday">{{ __('No Birthdays Yesterday') }}</div>

    <div class="muted-title-birthday">{{ __('Tomorrow') }}</div>
    <div class="birthday" v-for="TomBirthday in birthdays.tomorrow" :key="TomBirthday.member_name">
      <span class="birthday-value">{{TomBirthday.member_name}}, {{TomBirthday.club}}</span>
    </div>
    <div class="birthday" v-if="!birthdays.tomorrow">{{ __('No Birthdays Tomorrow') }}</div>

    <div class="heading">{{ __('Chat') }}</div>
    <a @click="open_chat">{{ __('Open Chat') }}</a>
  </div>
</template>
<script>
export default {
  data() {
    return {
      events: [],
      birthdays: []
    };
  },
  created() {
    this.get_events().then(events => {
      this.events = events;
    }),
      this.get_birthdays().then(birthdays => {
        this.birthdays = birthdays;
        console.log(birthdays.today);
      });
  },
  methods: {
    get_events() {
      const today = frappe.datetime.now_date();
      return frappe.xcall("frappe.desk.doctype.event.event.get_events", {
        start: today,
        end: today
      });
    },
    get_birthdays() {
      const today = frappe.datetime.now_date();
      return frappe.xcall(
        "pranali_reloaded.pranali_reloaded.api.get_birthdays",
        {
          start_date: today
        }
      );
    },
    open_chat() {
      setTimeout(frappe.chat.widget.toggle);
    },
    get_time(timestamp) {
      return frappe.datetime.get_time(timestamp);
    },
    open_event(event) {
      frappe.set_route("Form", "Event", event.name);
    }
  }
};
</script>
<style scoped>
.muted-title-birthday {
  margin-bottom: 5px;
  text-transform: uppercase;
  font-size: 10px;
  font-weight: 600;
  color: #8d99a6;
}
.birthday {
  padding-bottom: 5px;
}
.heading {
  text-transform: uppercase;
  font-size: 13px;
  font-weight: 600;
  margin: 8px 0;
}
.muted-title {
  margin-top: 5px;
}
</style>