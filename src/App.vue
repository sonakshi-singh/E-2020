<template >
  <div id="app">
    <router-view></router-view>
    <!-- <div v-if="travel=='Tokyo'">
      <h2>
        <br />Travelling to Tokyo ...Here is what you need to know
        <br />
        <br />
      </h2>
      <b-list-group style="opacity:.8" id="card">
        <b-list-group-item class="text-center">
          <SafetyRating :country="country" />
        </b-list-group-item>
        <b-list-group-item class="text-center">
          <KeyPhrases v-bind:phrases="phrases" />
        </b-list-group-item>
        <b-list-group-item title="Emergency Numbers" id="card">
          <h1 align="left">
            <b>Emergency</b> Numbers
          </h1>
          <h3>911</h3>
        </b-list-group-item>
        <b-list-group-item title="Tap Water">
          <h1 align="left">
            <b>Tap Water</b>
          </h1>
          <h3>Safe</h3>
        </b-list-group-item>
        <b-list-group-item title="Languages">
          <h1 align="left">
            <b>Languages</b>
          </h1>
          <h3>Japanese</h3>
        </b-list-group-item>
        <b-list-group-item title="Outlets">
          <h1 align="left">
            <b>Outlets</b>
          </h1>
          <h3>Type A or B</h3>
        </b-list-group-item>
        <b-list-group-item>
          <Vaccinations v-bind:vaccination="vaccination" />
        </b-list-group-item>
        <b-list-group-item title="Pag List">
          <h1 align="left">
            <b>Packing List</b>
          </h1>
          <h3>Toothbrush</h3>
        </b-list-group-item>
        <b-list-group-item title="Local Healthcare Expert Tips" class="text-center">
          <h1 align="left">
            <b>Local Healthcare Expert Tips</b>
          </h1>
          <h3>Try some sushi!</h3>
        </b-list-group-item>
        <b-list-group-item class="text-center">
          <DrugSearch v-bind:drugs="drugs" />
        </b-list-group-item>
      </b-list-group>
    </div>-->
  </div>
</template>

<script>

export default {
  name: "App",
  data() {
    return {};
  },
  components: {
  }
};
</script>

<style >
html, body, #app, #app>div {
  height: 100%;
  background-color: #F8F8F8;

}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
   padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100%;
}

</style>
