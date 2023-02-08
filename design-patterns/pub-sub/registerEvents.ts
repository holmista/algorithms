import MyEvent from "./MyEvent.js";
import events from "./createEvents.js";

function register() {
  events.forEach((event) => {
    MyEvent.addEvent(event.eventName);
    event.callbacks.forEach((callback) => {
      MyEvent.addEventListener(event.eventName, callback);
    });
  });
}

export default register;
