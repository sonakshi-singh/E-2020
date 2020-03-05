<template>
  <b-container fluid class="home-container">
    <div class="home-container">
      <b-row>
        <b-col sm="12" md="12" lg="12" xl="12">
          <h1>WHERE ARE YOU GOING ?</h1>
          <input type="text" v-model="travel" align="center" placeholder="Enter City Name Here" />
          <div>{{travel}}</div>
        </b-col>
      </b-row>
      <b-row>
        <b-col sm="6" md="12" lg="3" xl="3">
          <router-link :to="'drugSearch'">
            <b-button variant="success" @click="destEntered">Find OTC Medicine Equivalent</b-button>
          </router-link>
        </b-col>
        <b-col sm="6" md="12" lg="3" xl="3">
          <b-button variant="info">Find Pharmacies</b-button>
        </b-col>
        <b-col sm="6" md="12" lg="3" xl="3">
          <router-link :to="'factSheet'">
            <b-button variant="warning" @click="destEntered">Traveler Factsheet</b-button>
          </router-link>
        </b-col>
        <b-col sm="6" md="12" lg="3" xl="3">
          <router-link :to="'keyPhrases'">
            <b-button variant="warning" @click="destEntered">Medical Phrasebook</b-button>
          </router-link>
        </b-col>
      </b-row>
    </div>
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
.home-container {
  background-image: url("../assets/background.jpg");
}
</style>


