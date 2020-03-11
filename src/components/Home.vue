<template>
  <div>
    <Banner></Banner>
    <b-container fluid class="home-container">
      <div class="enter-dest">
        <b-row>
          <b-col xs="12" sm="12" md="9" offset-md="2" lg="6" offset-lg="3" xl="6" offset-xl="3">
            <div class="content">
              <h1>WHERE ARE YOU GOING ?</h1>
              <b-form-select v-model="travel" :options="options"></b-form-select>
              <!-- <div class="mt-3">
                Selected:
                <strong>{{ travel }}</strong>
              </div> -->
              <!-- <b-form-input
                type="text"
                v-model="travel"
                align="center"
                placeholder="Enter City Name Here"
                class="input"
              ></b-form-input>-->
            </div>
          </b-col>
        </b-row>
      </div>
      <div class="buttons">
        <b-row no-gutters>
          <b-col xs="6" sm="6" md="6" lg="3" xl="3">
            <router-link :to="'drugSearch'">
              <b-button
                variant="success"
                @click="destEntered"
                class="nav-buttons"
                :disabled="!travel"
              >Find OTC Medicine Equivalent</b-button>
            </router-link>
          </b-col>
          <b-col xs="6" sm="6" md="6" lg="3" xl="3">
            <b-button variant="info" disabled>Find Pharmacies</b-button>
          </b-col>
          <b-col xs="6" sm="6" md="6" lg="3" xl="3">
            <router-link :to="'factSheet'">
              <b-button
                variant="warning"
                @click="destEntered"
                :disabled="!travel"
              >Traveler Factsheet</b-button>
            </router-link>
          </b-col>
          <b-col xs="6" sm="6" md="6" lg="3" xl="3">
            <router-link :to="'keyPhrases'">
              <b-button
                variant="warning"
                @click="destEntered"
                :disabled="!travel"
              >Medical Phrasebook</b-button>
            </router-link>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>

<script>
import Banner from "./Banner.vue";

export default {
  name: "Home",
  data() {
    return {
      travel: null,
      options: [
        { value: null, text: "Please select a destination" },
        { value: "Tokyo", text: "Tokyo" }
      ]
    };
  },
  methods: {
    destEntered() {
      console.log("is it even reaching");
      this.$root.$emit("destWasEntered", this.travel);
    }
  },
  components: {
    Banner
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

  .buttons {
    position: relative;
    top: 20%;
    transform: translateY(-50%);
    display: inline;
  }

  .enter-dest {
    position: relative;
    top: 20%;
    transform: translateY(-50%);

    .content {
      margin: 2em 0 0 0;
    }

    .input {
      margin: 1em 0 0 0;
    }
  }
}

.btn-warning,
.btn-success,
.btn-info {
  background-color: $button-color;
  background-image: linear-gradient(315deg, #e7eff9 0%, #cfd6e6 74%);
  border-color: darken($button-color, 15%);
  color: darken($button-color, 50%);
  height: 8em;
  word-break: break-word;
  width: 50%;
}
</style>


