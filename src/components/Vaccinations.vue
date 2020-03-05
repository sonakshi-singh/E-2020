<template>
  <div class="hello">
    <h1 align="left"><b>Vaccinations recommended for travel</b></h1>
    <div v-bind:key="vac.id" v-for="vac in vaccination">
      <p align="left">
       <b> 
      <input type="checkbox" align="left">
        {{vac.vacc}}
      </b>
      </p>
    </div>
  
  </div>
</template>

<script>
export default {
  name: 'Vaccinations',
  props: ["vaccination"]
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
