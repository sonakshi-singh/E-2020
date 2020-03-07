<template>
  <b-container fluid class="factSheet-container">
    <Banner></Banner>
    <b-row>
      <b-col xs="6" sm="6" md="6" lg="6" xl="6">
        <h1 align="left">
          <b>Key Phrases in Japanese</b>
        </h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col xs="6" sm="6" md="6" lg="6" xl="6">
        <div v-bind:key="phrase.id" v-for="phrase in phrases">
          <p align="left">
            <b>English: {{phrase.English}} <br>Japanese: {{phrase.Japanese}}  <br>Pronunciation: {{phrase.Pronunciation}} <b-icon-volume-up-fill></b-icon-volume-up-fill></b>
          </p>
        </div>
      </b-col>
    </b-row>
    <Footer></Footer>
  </b-container>
</template>

<script>
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";
import json from "../../Phrases.json"
export default {
  name: "KeyPhrases",
  data() {
    return {
      phrases: json["Sheet1"],
      phrase: "",
      destination: ""
    };
  },
  created() {
    this.testItOut();
  },
  methods: {
    testItOut() {
      this.$root.$on("destWasEntered", travel => {
        this.destination = travel;
        console.log("WAIT WHAT", this.destination);
      });
    }
  },
  components: {
    Banner,
    Footer
  }
};
</script>

<style>
* {
  font-family: "Montserrat", sans-serif;
  color: #333;
  text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);
}
</style>