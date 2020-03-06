<template>
  <b-navbar class="navbar navbar-expand-md navbar-dark bg-dark fixed-bottom">
    <b-navbar-nav class="collapse navbar-collapse" id="navbarCollapse">
      <b-nav-item>
        <router-link :to="'drugSearch'">OTC</router-link>
      </b-nav-item>
      <b-nav-item>
        <router-link :to="'factSheet'">FACT BOOK</router-link>
      </b-nav-item>
      <b-nav-item>PHARMACY</b-nav-item>
      <b-nav-item>
        <router-link :to="'keyPhrases'">PHRASING</router-link>
      </b-nav-item>
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
$page-color: #333;
$text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);

* {
  font-family: "Montserrat", sans-serif;
  color: $page-color;
  text-shadow: $text-shadow;
 
}

.bg-dark {
  background-color: white !important;
  -webkit-box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
  -moz-box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
  box-shadow: 0px -4px 14px -14px rgba(201, 201, 201, 1);
  bottom: 0;
    margin-top: calc(20% + 20px);
    position: relative;
    bottom: 0;
}

.navbar-nav {
  justify-content: center;
  text-decoration: none;
}
</style>
