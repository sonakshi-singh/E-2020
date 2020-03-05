<template>
  <b-navbar class="navbar navbar-expand-md navbar-dark bg-dark fixed-bottom">
    <b-navbar-nav class="collapse navbar-collapse" id="navbarCollapse">
      <b-nav-item href="#">OTC</b-nav-item>
      <b-nav-item href="#">FACT BOOK</b-nav-item>
      <b-nav-item href="#">PHARMACY</b-nav-item>
      <b-nav-item href="#">PHRASING</b-nav-item>
      <b-nav-item href="#">SETTINGS</b-nav-item>
   </b-navbar-nav>
  </b-navbar>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {};
  }
};
</script>
 
<style lang="scss" scoped>
.bg-dark {
  background-color: white !important;
  -webkit-box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
  -moz-box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
  box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
}

.navbar-nav {
    justify-content: center;
}

</style>
