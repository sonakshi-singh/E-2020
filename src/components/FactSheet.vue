<template>
  <b-container fluid class="factSheet-container">
    <Banner></Banner>
    <div v-if="destination === 'Tokyo'">
      <button @click="generate_pdf">Generate PDF </button>
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
            <SafetyRating :country="country" />
          </b-col>
        </b-row>
        <p></p>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">EMERGENCY NUMBERS</p>
            <p class="content">110 - Crime and accident</p>
            <p class="content">119 - Fire and ambulance</p>
            <p class="heading">CLOSEST EMBASSY</p><br>
            <Embassies :city="Tokyo"/>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">WATER SAFETY</p>
            <p class="content">Tap water is safe for direct consumption</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">LANGUAGES</p>
            <p class="content">Japanese is the main language</p>
            <p class="content">Most Japanese speak limited English unless you are at popular tourist spots</p>
          </b-col>
        </b-row>
      </div>
      <hr />
      <div>
        <b-row>
          <b-col xs="6" sm="6" md="6" lg="6" xl="6">
            <p class="heading">OUTLETS</p>
            <p class="content">Type A or B</p>
            <Outlets/>
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
    <Footer></Footer>
  </b-container>
</template>


<script>
import Vaccinations from "./Vaccinations.vue";
import SafetyRating from "./SafetyRating.vue";
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";
import Embassies from "./Embassies.vue"
import Outlets from "./Outlets.vue"
import jspdf from "jspdf"   

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
    },
  generate_pdf(){
      console.log("reached this spot")
      const doc=new jspdf()  
      doc.text("Fact Sheet Bitches",15,15)
      doc.save("Bene_Travel.pdf")
    }},
  components: {
    Vaccinations,
    SafetyRating,  
    Banner,
    Footer,
    Embassies,
    Outlets
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


