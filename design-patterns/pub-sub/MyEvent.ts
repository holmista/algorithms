class MyEvent {
  static events = new Map<string, Function[]>();
  static addEvent(eventName: string) {
    this.events.set(eventName, [() => {}]);
  }
  static addEventListener(eventName: string, callback: Function) {
    if (this.events.has(eventName)) {
      const callbacks = this.events.get(eventName) as Function[];
      this.events.set(eventName, [...callbacks, callback]);
    } else throw new Error("Event not found");
  }
  static dispatchEventAsync(eventName: string) {
    if (this.events.has(eventName)) {
      const callbacks = this.events.get(eventName) as Function[];
      callbacks.forEach((callback) => callback());
    } else throw new Error("Event not found");
  }
  static async dispatchEventSync(eventName: string) {
    if (this.events.has(eventName)) {
      const callbacks = this.events.get(eventName) as Function[];
      for (const callback of callbacks) {
        await callback();
      }
    } else throw new Error("Event not found");
  }
}
export default MyEvent;
