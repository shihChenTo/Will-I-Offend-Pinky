<template>
  <span v-html="resultString" />
</template>

<script>
export default {
  name: 'OneHistory',
  props: {content: {type: String, required:true}},
   setup(props) {
    let toSearch = props.content.match(/\[\[.*?\]\]/g)
    let resultString = props.content
    toSearch.forEach(element => {
      let searchString = element.replace("[[", "").replace("]]", "");
      resultString = resultString.replace(element, `<a target="_blank" href="https://zh.wikipedia.org/wiki/${searchString}">${searchString}</a>`);
    })
    return {resultString: resultString}
  },
};
</script>

<style>
  a:link{color:#304ffe;}
  a:visited{color:#0026ca;}
  a:hover{color:#2962ff;} 
</style>