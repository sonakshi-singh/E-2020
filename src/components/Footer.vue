<template>
  <b-navbar class="navbar navbar-expand-md navbar-dark bg-dark fixed-bottom">
    <b-navbar-nav class="collapse navbar-collapse" id="navbarCollapse">
      <b-row>
        <b-col sm="2" md="2" lg="2" xl="2">
          <b-nav-item>
            <router-link :to="'drugSearch'">
              <hospital-icon />
              <div>OTC</div>
            </router-link>
          </b-nav-item>
        </b-col>
        <b-col sm="3" md="3" lg="3" xl="3">
          <b-nav-item>
            <router-link :to="'factSheet'">
              <book-icon />
              <div>FACT BOOK</div>
            </router-link>
          </b-nav-item>
        </b-col>
        <b-col sm="3" md="3" lg="3" xl="3">
          <b-nav-item>
            <map-marker-icon />
            <div>PHARMACY</div>
          </b-nav-item>
        </b-col>
        <b-col sm="2" md="2" lg="2" xl="2">
          <b-nav-item>
            <router-link :to="'keyPhrases'">
              <message-text-outline-icon />
              <div>PHRASES</div>
            </router-link>
          </b-nav-item>
        </b-col>
        <b-col sm="2" md="2" lg="2" xl="2">
          <b-nav-item>
            <dots-horizontal-icon />
            <div>SETTINGS</div>
          </b-nav-item>
        </b-col>
      </b-row>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
import HospitalIcon from "mdi-vue/Hospital";
import BookIcon from "mdi-vue/Book";
import MapMarkerIcon from "mdi-vue/MapMarker";
import MessageTextOutlineIcon from "mdi-vue/MessageTextOutline";
import DotsHorizontalIcon from "mdi-vue/DotsHorizontal";

export default {
  name: "Footer",
  data() {
    return {};
  },
  components: {
    HospitalIcon,
    BookIcon,
    MapMarkerIcon,
    MessageTextOutlineIcon,
    DotsHorizontalIcon
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
  margin-top: calc(10% + 20px);
  position: relative;
  bottom: 0;
}

.navbar-nav {
  justify-content: center;
  text-decoration: none;
}
</style>
