<template>
  <div class="ratingBox"><br>
    <div v-bind:key="vac" v-for="vac in vaccinations">
      <p align="left">
      <input type="checkbox" align="left">  {{vac}}</p>
    </div>
  </div>
</template>

<script>
import vac from '../../vaccines.json'
export default {
  name: 'Vaccinations',
  data(){
      return{
          vaccinations: vac
      }
  },
  created: function() {
    var len = this.vaccinations.length
    var strlen = 0
    var vac

    for (var i=0; i<len; i++){
      if (this.vaccinations[i] == "\nRoutine vaccines\n"){
        this.vaccinations[i] = "\nOther Routine Vaccines\n"
        vac = this.vaccinations[i]
        this.vaccinations[i] = this.vaccinations[len-1]
        this.vaccinations[len-1] = vac
      }
      strlen = this.vaccinations[i].length
      this.vaccinations[i] = this.vaccinations[i].substring(1,strlen-1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
.content {
    margin: 1em 0 0 0;
    @include font-weight(400);
    display: list-item; /* This has to be "list-item"                                               */
    list-style-type: disc; /* See https://developer.mozilla.org/en-US/docs/Web/CSS/list-style-type     */
    list-style-position: inside;
  }
</style>
