<template>
  <div class="drugs">
    <h2 align="left"><b>Please enter below the drug whose information you seek</b></h2>
     <div>
      <p align="left">
      <b>
      <input type="text" v-model="input1" align="left" placeholder="Enter Drug Name Here">   
      <!-- <button type="submit"  >Submit</button> -->
      </b>
      </p>
         <div v-if="input1!=''"> 
         <div v-bind:key="drug.id" v-for="drug in drugs">
            <div v-if="(drug.drug==input1.toLowerCase())">
                <p align="left" >
                <b>
                <br />
                Drug :  {{drug.drug}}
                <br />
                Generic Name : {{drug.Generic_Name}}
                <br />
                Strength : {{drug.Strength}},
                <br />
                Availability : {{drug.Availability}},
                <br />
                Drug_Class : {{drug.Drug_Class}},
                <br />
                Alternate Drug Options : {{drug.Alternate}}
                </b>
                </p>
                </div> 
            </div>    
        </div> 
        <div v-else align="left">
            <b>Please input data to get results....</b>
            </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'DrugSearch',
  props: ["drugs"],
  data(){
      return{
         input1:""   
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

$base-color: #42b983;

.is-Complete{
  text-decoration:line-through;
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
