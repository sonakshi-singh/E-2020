<template>
  <div class="drugs">
    <h3 align="left">Please enter below the drug whose information you seek</h3>
     <div>
      <p align="left">
      <input type="text" v-model="input1" align="left" placeholder="Enter Drug Name Here">   
      <button type="submit"  >Submit</button>
      </p>
      {{input1}}
         <div v-bind:key="drug.id" v-for="drug in drugs">
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
<style scoped>

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
