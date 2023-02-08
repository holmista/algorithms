const events = ["test", "log_in_user"] as const;

type event = typeof events[number];

interface IEvent {
  eventName: event;
  callbacks: Array<Function>;
}

const testEvent: IEvent = {
  eventName: "test",
  callbacks: [
    function (): Promise<void> {
      return new Promise((resolve) => {
        setTimeout(() => {
          console.log("listening for test event 1");
          resolve();
        }, 3000);
      });
    },
    function () {
      console.log("listening for test event 2");
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
