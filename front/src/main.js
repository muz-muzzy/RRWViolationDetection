import { createApp } from "vue";
import App from "./App.vue";
import { createVuestic } from "vuestic-ui";
import './style.css'
import "vuestic-ui/css";
import "material-design-icons-iconfont/dist/material-design-icons.min.css";

createApp(App).use(createVuestic()).mount("#app");