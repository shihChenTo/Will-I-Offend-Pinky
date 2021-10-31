import { createApp } from 'vue'
import { Space, DatePicker, Typography, Layout, Grid, Col, Row, Icon, Divider} from 'ant-design-vue';
// import 'ant-design-vue/lib/button/style';
import App from './App.vue'

createApp(App)
.use(Space)
.use(DatePicker)
.use(Typography)
.use(Layout)
.use(Grid)
.use(Col)
.use(Row)
.use(Icon)
.use(Divider)
.mount('#app')
