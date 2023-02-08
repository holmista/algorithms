import registerEvents from "./registerEvents.js";
registerEvents();
import testEvents from "./testEvents.js";
testEvents();

// function a(): Promise<string> {
//   return new Promise((resolve) => {
//     setTimeout(() => {
//       resolve("a");
//     }, 3000);
//   });
// }

// function b() {
//   return "b";
// }

// const functions = [a, b];
// for (const func of functions) {
//   const result = await func();
//   console.log(result);
// }
