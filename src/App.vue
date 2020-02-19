<template >
  <div id="app">
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg"> -->
    <h1>Where are you Travelling ???</h1>
     <input type="text" v-model="travel" align="center" placeholder="Enter City Name Here">   
      <!-- <button type="submit"  >Submit</button> -->
    <div v-if="travel=='Tokyo'"> 
      <h2>Travelling to Tokyo ...Here is what you need to know</h2>
      <HelloWorld v-bind:vaccination="vaccination"/>
      <DrugSearch v-bind:drugs="drugs" />
    </div>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import DrugSearch from './components/DrugSearch.vue'

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
      travel:""
    }   
  },
  components: {
    HelloWorld,
    DrugSearch
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
  color: #2c3e50;
  margin-top: 60px;
}

</style>
