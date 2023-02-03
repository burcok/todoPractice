<template>
  <div class="bg-gray-800">
    <div
      style="min-height: 100vh"
      class="bg-gray-800 py-20 px-16 sm:px-32 lg:px-64 w-screen"
    >
      <taskList />
    </div>
  </div>
</template>
<script>
import taskList from "./components/taskList.vue";

export default {
  components: {
    taskList,
  },
};
</script>
<!--  

  TODO: Düzenle kısmı yapılacak
  TODO: Sildikten sonraki animasyon düzelicek

-->

<style>
.unselectable {
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -moz-text-size-adjust: none;
  -webkit-text-size-adjust: none;
  text-size-adjust: none;
  font-family: system-ui, "Segoe UI", Roboto, Cantarell, "Helvetica Neue", Helvetica,
    Arial, sans-serif;
  line-height: 1.75;
}
#app {
  overflow-x: hidden;
}
</style>
