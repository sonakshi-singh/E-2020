<template >
  <div id="app">
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg"> -->
    <h1 style="font-size:60px;">Welcome to Bene</h1>
    <h1>Where are you Travelling ?</h1>
     <input type="text" v-model="travel" align="center" placeholder="Enter City Name Here">   
      <!-- <button type="submit"  >Submit</button> -->
    <div v-if="travel=='Tokyo'"> 
      <h2><br>Travelling to Tokyo ...Here is what you need to know<br><br></h2>
      <b-card-group deck style = "opacity:.8">
      <b-card class="text-center">
        <SafetyRating :country = "country" />
      </b-card>
      <b-card class="text-center">
        <KeyPhrases v-bind:phrases="phrases" />
      </b-card>
      <b-card class="text-center">
        <HelloWorld v-bind:vaccination="vaccination" />
      </b-card>
      <b-card class="text-center">
        <DrugSearch v-bind:drugs="drugs" />
      </b-card>
      </b-card-group>
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import DrugSearch from './components/DrugSearch.vue'
import KeyPhrases from './components/KeyPhrases.vue'
import SafetyRating from './components/SafetyRating.vue'


export default {
  name: 'App',
  data(){
    return{
      vaccination: [
        { id:1,
          vacc:"Hepatitis A"},
          { id:2,
          vacc:"Hepatitis B"},
          { id:3,
          vacc:"Japanese encephalitis"},
          { id:4,
          vacc:"Rabies"},
          { id:5,
          vacc:"Polio"},
          { id:6,
          vacc:"Measels"},
          { id:7,
          vacc:"Shingles"}          // "hepatitis B", "typhoid", "Japanese encephalitis", "rabies", "meningitis", "polio", "measles", "mumps and rubella (MMR)", "Tdap (tetanus, diphtheria and pertussis)", "chickenpox", "shingles", "pneumonia" ,"influenza"]
      ],
      drugs:[
        { id:1,
          drug:"advil",
          Generic_Name:"ibuprofen",
          Strength:"200 mg",
          Availability:"Rx and/or OTC",
          Drug_Class:"Nonsteroidal anti-inflammatory drugs",
          Alternate:"イブ (Eve): ibuprofen tablets"},
          { id:2,
          vacc:"hepatitis B"},
          { id:3,
          vacc:"Japanese encephalitis"},
          { id:4,
          vacc:"rabies"},
          { id:5,
          vacc:"polio"},
          { id:6,
          vacc:"measels"},
          { id:7,
          vacc:"shingles"} 
      ],
      phrases: [
        { id:1,
          eng_phrase:"Hello",
          trans_phrase:"Konnichiwa"},
        { id:2,
          eng_phrase:"Goodbye",
          trans_phrase:"Sayonara"},
        { id:3,
          eng_phrase:"Yes",
          trans_phrase:"Hai"},
        { id:4,
          eng_phrase:"No",
          trans_phrase:"Lie"},
        { id:5,
          eng_phrase:"Please",
          trans_phrase:"Onegaishimasu"},
        { id:6,
          eng_phrase:"Thank You",
          trans_phrase:"Domo Arigato"}
      ],
      country: "Japan",
      travel:""
    }   
  },
  components: {
    HelloWorld,
    DrugSearch,
    KeyPhrases,
    SafetyRating
  }
}
</script>

<style >
#app { 
  /* background-image: url("./body.jpg");
  background-size: length; */
  /* background-color: darkslategray; */
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:black;
  margin-top: 60px;
}

</style>
