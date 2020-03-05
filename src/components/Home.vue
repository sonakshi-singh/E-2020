<template>
  <b-container fluid class="home-container">
    <b-row>
      <b-col sm="12" md="12" lg="12" xl="12">
        <h1>WHERE ARE YOU GOING ?</h1>
        <input type="text" v-model="travel" align="center" placeholder="Enter City Name Here" />
        <div>{{travel}}</div>
      </b-col>
    </b-row>
    <b-row>
      <b-col xs="6" sm="6" md="6" lg="3" xl="3">
        <router-link :to="'drugSearch'">
          <b-button variant="success" @click="destEntered" className="nav-buttons">Find OTC Medicine Equivalent</b-button>
        </router-link>
      </b-col>
      <b-col xs="6" sm="6" md="6" lg="3" xl="3">
        <b-button variant="info">Find Pharmacies</b-button>
      </b-col>
      <b-col xs="6" sm="6" md="6" lg="3" xl="3">
        <router-link :to="'factSheet'">
          <b-button variant="warning" @click="destEntered">Traveler Factsheet</b-button>
        </router-link>
      </b-col>
      <b-col xs="6" sm="6" md="6" lg="3" xl="3">
        <router-link :to="'keyPhrases'">
          <b-button variant="warning" @click="destEntered">Medical Phrasebook</b-button>
        </router-link>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: "Home",
  data() {
    return {
      travel: ""
    };
  },
  methods: {
    destEntered() {
      console.log("is it even reaching");
      this.$root.$emit("destWasEntered", this.travel);
    }
  }
};
</script>

<style lang="scss" scoped>
$button-color: #e7eff9;

.home-container {
  background-image: url("../assets/background.jpg");
  background-repeat: no-repeat;
  background-position: center center;
  background-attachment: fixed;
  background-size: cover;
  height: 100%;
}

.btn-warning, .btn-success, .btn-info {
  background-color: $button-color;
  background-image: linear-gradient(315deg, #e7eff9 0%, #cfd6e6 74%);
  border-color: darken($button-color, 15%);
  color: darken($button-color, 50%);
  height:8em;
  word-break: break-word;
  width:50%;
}

</style>


