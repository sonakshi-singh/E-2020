<template>
  <b-container fluid class="factSheet-container">
    <Banner></Banner>
    <div v-if="destination === 'Tokyo'" class="country-info">
      <b-row>
        <b-col xs="6" sm="6" md="6" lg="6" xl="6">
          <p class="tokyo-heading">{{upperCaseDest}} TRAVEL FACTSHEET</p>
        </b-col>
        <b-col xs="3" sm="3" md="3" lg="3" xl="3">
          <p class="download-heading">DOWNLOAD</p>
        </b-col>
      </b-row>
      <br />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">SAFETY RATING</p>
          </b-col>
        </b-row>
        <p></p>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">EMERGENCY NUMBERS</p>
            <p class="content">911</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">WATER SAFETY</p>
            <p class="content">Safe to drink tap water</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">LANGUAGES</p>
            <p class="content">Japanese</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">OUTLETS</p>
            <p class="content">Type A or B</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">VACCINATION REQUIREMENTS</p>
          </b-col>
        </b-row>
        <div>
          <Vaccinations v-bind:vaccination="vaccination" />
        </div>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">LOCAL TIPS</p>
            <p class="content">Try some Sushi!</p>
          </b-col>
        </b-row>
      </div>
    </div>
    <safety-rating></safety-rating>
    <Footer></Footer>
  </b-container>
</template>


<script>
import Vaccinations from "./Vaccinations.vue";
import SafetyRating from "./SafetyRating.vue";
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";

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
      destination: "Tokyo",
      upperCaseDest: "TOKYO",
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
    SafetyRating,  
    Banner,
    Footer
  }
};
</script>

<style lang="scss" scoped>
@mixin font-weight($font-weight) {
  font-weight: $font-weight;
  text-align: left;
}

* {
  font-family: "Montserrat", sans-serif;
  color: #333;
  text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);
 
}

.factSheet-container {

  .download-heading {
    color: lighten(#333, 20%);
    text-align: left;
  }

  .tokyo-heading {
    @include font-weight(800);
    letter-spacing: 2px;
  }

  .country-info {
    margin: 1em 0 0 0;
  }

  .heading {
    margin: 2em 0 0 0;
    @include font-weight(600);
  }

  .content {
    margin: 1em 0 0 0;
    @include font-weight(400);
    display: list-item; /* This has to be "list-item"                                               */
    list-style-type: disc; /* See https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type     */
    list-style-position: inside;
  }

  hr {
  border-color: lightgray transparent #474747 transparent;
  
  border-style: solid;
  height: 0;
  }
}
</style>


