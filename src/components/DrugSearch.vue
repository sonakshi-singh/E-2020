<template>
  <div class="drugs">
    <Banner />
    <h1 align="left">
      <b>Please enter below the drug whose information you seek</b>
    </h1>
    <div>
      <p align="left">
        <b>
          <input type="text" v-model="input1" align="left" placeholder="Enter Drug Name Here" />
<<<<<<< HEAD
          <button type="submit"  >Submit</button> 
        

     
=======
          <!-- <button type="submit"  >Submit</button> -->
        </b>
      </p>
>>>>>>> be868cdaf69257d46788bbb79fc7339fb8ad89ca
      <div v-if="input1!=''">
        <div v-bind:key="drug.id" v-for="drug in drugs">
          <div v-if="(drug.drug==input1.toLowerCase())">
            <p align="left">
              <b>
                <br />
                Drug : {{drug.drug}}
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
<<<<<<< HEAD

                </b>
                </p>
                </div> 
            </div>    
        </div> 


       <div v-else align="left">
            <b>Please input data to get results....</b>
            </div> 

    </div>
  


            
  </div> -->

=======
              </b>
            </p>
          </div>
        </div>
      </div>
      <div v-else align="left">
        <b>Please input data to get results....</b>
      </div>
    </div>
    <Footer></Footer>
  </div>
>>>>>>> be868cdaf69257d46788bbb79fc7339fb8ad89ca
</template>

<script>
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";

export default {
  name: "DrugSearch",
  props: ["drugs"],
<<<<<<< HEAD

  data(){
      return{
        input1: "",
         destination:"" ,
         selected:""
      };

=======
  data() {
    return {
      input1: "",
      destination: ""
    };
>>>>>>> be868cdaf69257d46788bbb79fc7339fb8ad89ca
  },
  created() {
    this.$root.$on("destWasEntered", travel => {
      this.destination = travel;
      console.log("dest", this.destination);
    });
  },
  

    components: {
    Banner,
    Footer
  }
<<<<<<< HEAD
  
  }
}; 
  


 



=======
};
>>>>>>> be868cdaf69257d46788bbb79fc7339fb8ad89ca
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

* {
  font-family: "Montserrat", sans-serif;
  color: #333;
  text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);
 
}
$base-color: #42b983;

.is-Complete {
  text-decoration: line-through;
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
<<<<<<< HEAD
}

$base-color : #E70B28;
/*
.logo
{
  display: inline-block;
  width: 10%;
 
}

.b-navbar
{
  height: 10px;
  display: inline-block;
  width: 30%;
  height: 40%;
  
}
*/
@import url('https://fonts.googleapis.com/css?family=Montserrat&display=swap');
p{
font-family: 'Montserrat';
color:#808080;
font-weight: bold;
padding-top: 5px;
margin-left: 2.5%;



}
input
{
  width: 50%;
  border-radius: 15px;
  padding: 5px;
  background-color:	#EFEFEF ;
  margin-left: 25%;
=======
>>>>>>> be868cdaf69257d46788bbb79fc7339fb8ad89ca
}
</style>
