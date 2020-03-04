<template>
  <b-container fluid class="home-container">
    <div v-if="{destination}">
      <h2>
        <br />
        Travelling to {{destination}} ...Here is what you need to know
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
      </b-list-group>
    </div>
  </b-container>
</template>


<script>
import Vaccinations from "./Vaccinations.vue";
import SafetyRating from "./SafetyRating.vue";

export default {
  name: "FactSheet",
  data() {
    return {
      vaccination: [
        { id: 1, vacc: "Hepatitis A" },
        { id: 2, vacc: "Hepatitis B" },
        { id: 3, vacc: "Japanese encephalitis" },
        { id: 4, vacc: "Rabies" },
        { id: 5, vacc: "Polio" },
        { id: 6, vacc: "Measels" },
        { id: 7, vacc: "Shingles" } // "hepatitis B", "typhoid", "Japanese encephalitis", "rabies", "meningitis", "polio", "measles", "mumps and rubella (MMR)", "Tdap (tetanus, diphtheria and pertussis)", "chickenpox", "shingles", "pneumonia" ,"influenza"]
      ],
      destination: "",
      country: "Hong Kong"
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
    Vaccinations,
    SafetyRating
  }
};
</script>

<style lang="scss" scoped>
.home-container {
  background-image: url("../assets/background.jpg");
}
</style>


