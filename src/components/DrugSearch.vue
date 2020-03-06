<template>

  <b-container fluid class="drugs-container">
   <Banner></Banner>



  <!-- Image and text -->
  

<div>
<p align="left"> SEARCH BY </p>
<b-input-group>
  <input type="text" v-model="input1" align="left" placeholder="Search by US medication name"/> 
  <b-input-group-append>
 <b-icon-search> </b-icon-search>
 </b-input-group-append>
</b-input-group>
<br><br>
<p align="center"> --- OR ---</p>
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


<div>
  
  <b-dropdown text="CATEGORY" 
    block
    variant="white"
    class="m-2" menu-class="w-100">
 
    <b-form-group>
    <b-dropdown-item href="#"> <b-form-radio v-model="selected" name="some-radios" value="A">COLD</b-form-radio> </b-dropdown-item>
    <b-dropdown-item href="#"> <b-form-radio v-model="selected" name="some-radios" value="B">FEVER</b-form-radio> </b-dropdown-item>
    <b-dropdown-item href="#"> <b-form-radio v-model="selected" name="some-radios" value="C">COUGH</b-form-radio> </b-dropdown-item>
    </b-form-group>
  </b-dropdown>
</div>

</div>
  <!--
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

                </b>
                </p>
                </div> 
            </div>    
        </div> 
        <div v-else align="left">
            <b>Please input data to get results....</b>
<<<<<<< HEAD
            </div> 

    
  


          
    
    -->

     <div>
      <b-button variant="info">SHOW RESULTS</b-button>
    </div> 


     
     <Footer></Footer>
  </b-container>
</template>

<script>
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";
export default {
  name: "DrugSearch",
  props: ["drugs"],
  data(){
      return{
        input1: "",
         destination:"" ,
         selected:""
      };
  },
 
  methods:{
  created() {
    this.$root.$on("destWasEntered", travel => {
      this.destination = travel;
      console.log("dest", this.destination);
    });
  }
  },
  components: {
    Banner,
    Footer
  }
  
};
 
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
* {
  font-family: "Montserrat", sans-serif;
  color: #333;
  text-shadow: 0px 1px 0px rgba(255, 255, 255, 0.3),
    0px -0px 0px rgba(0, 0, 0, 0.7);
 
}
/*$base-color: #42b983;
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
}
*/
/*
.logo
{
  display: inline-block;
  width: 10%;
 
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
}
b-dropdown
{
  margin-left:10% ;
  width: 50%;
  background-color: white;
}
.btn-info{

background-color: #EF2942;
}
</style>
