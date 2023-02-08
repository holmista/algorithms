const events = ["test", "log_in_user"] as const;

type event = typeof events[number];

interface IEvent {
  eventName: event;
  callbacks: Array<Function>;
}

const testEvent: IEvent = {
  eventName: "test",
  callbacks: [
    () => {
      console.log("listening for test event");
    },
    () => {
      console.log("listening for test event again");
    },
  ],
};

const logInUserEvent: IEvent = {
  eventName: "log_in_user",
  callbacks: [
    () => {
      console.log("listening for log_in_user event");
    },
  ],
};

export default [testEvent, logInUserEvent];
