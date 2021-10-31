/* eslint-disable no-mixed-spaces-and-tabs */
<template>
  <a-layout class="layout">
    <a-layout-content 
      :style="{'background-color': mainColor,
               'padding-top': '50px'}"
    >
      <a-row
        type="flex"
        justify="center"
        style="padding: 50px 0"
      >
        <a-col
          :xs="{ span: 22 }"
          :md="{ span: 16}"
          align="center"
        >
          <a-space
            direction="vertical"
            align="center"
            size="middle"
          >
            <a-space
              direction="horizontal"
              align="baseline"
            >
              <span style="ont-weight: 300; font-size: 16px">在</span>
              <a-date-picker
                :locale="locale"
                :format="displayDateFormat"
                :value="date"
                @change="datePickerChange"
              />
            </a-space>
            <a-space
              direction="vertical"
              align="center"
            >
              <template v-if="Object.keys(dataOfTheDay.value).length != 0">
                <a-typography-paragraph style="font-weight: 300; font-size: 32px;">
                  你有可能冒犯到<span class="gaussian-blur">小粉红😅</span>
                </a-typography-paragraph>
              </template>
              <template v-else>
                <a-typography-paragraph style="font-weight: 300; font-size: 32px;">
                  你似乎不会冒犯到<span class="gaussian-blur">小粉红🥳</span>
                </a-typography-paragraph>
                <a-typography-paragraph>
                  不过，保险起见，还是去维基百科上看看吧？
                </a-typography-paragraph>
              </template>
            </a-space>
          </a-space>
        </a-col>
      </a-row>
      <a-row
        type="flex"
        justify="center"
      >
        <a-col
          :xs="{ span: 22 }"
          :md="{ span: 12}"
        >
          <a-space direction="vertical">
            <a-space direction="vertical">
              <template
                v-for="(category, category_index) in ['大事记', '出生','逝世','节假日和习俗']"
              >
                <template v-if="dataOfTheDay['value'][category] != null">
                  <a-typography-title
                    :key="category_index"
                    :level="3"
                  >
                    {{ category }}
                  </a-typography-title>
                  <a-typography-paragraph :key="category_index">
                    <ul>
                      <li
                        v-for="(item) in dataOfTheDay['value'][category]"
                        :key="item"
                      >
                        <OneHistory :content="item" />
                      </li>
                    </ul>
                  </a-typography-paragraph>
                </template>
              </template>
            </a-space>
          </a-space>
        </a-col>
      </a-row>
      <a-row
        type="flex"
        justify="center"
      >
        <a-col
          :xs="{ span: 22 }"
          :md="{ span: 12}"
          style="text-align: center; padding-top: 50px"
        >
          <a-divider />
          <a-typography-paragraph>
            <a
              target="_blank"
              :href="wikipediaThisDay"
            ><SearchOutlined /> 查看维基百科 </a>  <span style="padding: 0 5px">|</span> <a
              target="_blank"
              href="https://github.com/shihChenTo/Will-I-Offend-Pinky/issues"
            ><PullRequestOutlined /> 提交需要注意的数据</a>
          </a-typography-paragraph>
          <a-typography-paragraph type="secondary">
            <small>数据来自维基百科“历史上的今天”系列条目与网友贡献，不代表作者立场</small>
          </a-typography-paragraph>
        </a-col>
      </a-row>
    </a-layout-content>
    
    <a-layout-footer
      style="text-align: center"
      :style="{'background-color': lightColor}"
    >
      “各美其美，美人之美，美美与共，天下大同”<br>释甄铎 ©2021
    </a-layout-footer>
  </a-layout>
</template>

<script>
import moment from "moment";
import "moment/dist/locale/zh-cn";
import locale from "ant-design-vue/es/date-picker/locale/zh_CN";
import { defineComponent, ref, reactive } from "vue";
import OneHistory from "./OneHistory.vue";
import {
  SearchOutlined,
  PullRequestOutlined
} from '@ant-design/icons-vue';


export default defineComponent({
  components: {
    OneHistory,
    SearchOutlined,
    PullRequestOutlined
  },
  setup() {
    // const dateFormat = 'YYYY/MM/DD';
    const displayDateFormat = "M月D日";
    const dataJson = require("../../public/result.json");
    return {
      date: ref(moment()),
      displayDateFormat,
      moment,
      locale,
      dataJson,
      dataOfTheDay: reactive({value: {}}),
    };
  },
  data(){
    return{
      mainColor: "#fafafa",
      lightColor: "#fafafa",
      // dataOfTheDay: ref(this.dataJson[this.date.format('M月D日')])
    };
  },
  computed: {
    wikipediaThisDay() {
      return "https://zh.wikiedia.org/wiki/" + this.date.format('M月D日')
    },
    // dataOfTheDay() {
    //   let newData = reactive({});
    //   for(var key in this.dataJson[this.date.format('M月D日')]){
    //     newData[key] = reactive({});
    //     newData[key] = JSON.parse(JSON.stringify(this.dataJson[this.date.format('M月D日')][key]))
    //   }
    //   // let newData = {};
    //   // for(var key in this.dataJson[this.date.format('M月D日')]){
    //   //   console.log(this.dataJson[this.date.format('M月D日')][key])
    //   //   Vue.set(newData, key, this.dataJson[this.date.format('M月D日')][key])
    //   // }
    //   // newData = JSON.parse (JSON.stringify(this.dataJson[this.date.format('M月D日')]));
    //   // for (let i = 0; i < this.dataJson[this.date.format('M月D日')].length; i++) {
    //   //   this.$set(this.dataJson[this.date.format('M月D日')],i,this.dataJson[this.date.format('M月D日')][i])
    //   // }
    //   console.log(newData)
    //   return newData
    // }
  },
  watch: {
    date() {
      this.dataOfTheDay.value = this.dataJson[this.date.format('M月D日')]
      console.log(this.dataOfTheDay.value)
      console.log(Object.keys(this.dataOfTheDay.value).length)
      if(Object.keys(this.dataOfTheDay.value).length != 0) {
        this.mainColor = '#ef9a9a'
        this.lightColor = '#ffcccb'
      } else {
        this.mainColor = '#a5d6a7'
        this.lightColor = '#d7ffd9'
      }
    },
  },
  beforeMount() {
    this.date = moment();
  },
  methods: {
    datePickerChange(value) {
      if(value != null) {
        this.date = value;
      }
      
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ant-layout {
  min-height: 100%;
}
.gaussian-blur {
  -webkit-filter: blur(3px);
  -moz-filter: blur(3px);
  -o-filter: blur(3px);
  -ms-filter: blur(3px);
  filter: blur(3px); 
}
</style>
