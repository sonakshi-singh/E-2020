<template>
  <div>
    <Banner></Banner>
    <b-container fluid class="drugs-container">
      <!-- Image and text -->

      <div>
        <p align="left">SEARCH BY</p>
        <b-input-group>
          <input
            type="text"
            v-model="input1"
            align="left"
            placeholder="Search by US medication name"
          />
          <b-input-group-append>
            <b-icon-search></b-icon-search>
          </b-input-group-append>
        </b-input-group>
        <br />
        <br />
        <p align="center">--- OR ---</p>
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
<<<<<<< HEAD
                </p>
                </div> 
            </div>    
        </div> 
</div>

 <b-dropdown text="Category"
    block
    variant="white"
    class="m-2"
    menu-class="w-100">
  
  <div class="dropdown__menu">
  
     
      <div v-bind:key="category.id" v-for="category in categories">
    <div class="dropdown__menu-item">
      <input type="radio" v-model="picked" name="some-radios" value="A" style="margin-left:0%;padding:0%;">{{category.type}}
    </div>
      </div>
    
  </div>
  
  


</b-dropdown>



 
  <!--
=======
              </p>
            </div>
          </div>
        </div>

        <div>
          <b-dropdown text="CATEGORY" block variant="white" class="m-2" menu-class="w-100">
            <b-form-group>
              <div v-bind:key="category.id" v-for="category in categories">
                <b-dropdown-item href="#item">
                  <b-form-radio v-model="selected" name="some-radios" value="A">{{category.type}}</b-form-radio>
                </b-dropdown-item>
              </div>
            </b-form-group>
          </b-dropdown>
        </div>
      </div>
      <!--
>>>>>>> 240cf2ed52c83809cda0060bda7def693d5b4b2a
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
    </b-container>
    <Footer></Footer>
  </div>
</template>

<script>
import Banner from "./Banner.vue";
import Footer from "./Footer.vue";
import json from "../../categories.json";
export default {
  name: "DrugSearch",
  props: ["drugs"],
<<<<<<< HEAD
  data(){
      return{
        categories:json["medicinecategories"],
        category:"",
        input1: "",
         destination:"" ,
         picked:""
      };
=======
  data() {
    return {
      categories: json["medicinecategories"],
      category: "",
      input1: "",
      destination: "",
      selected: ""
    };
>>>>>>> 240cf2ed52c83809cda0060bda7def693d5b4b2a
  },

  methods: {
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

@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");
p {
  font-family: "Montserrat";
  color: #808080;
  font-weight: bold;
  padding-top: 5px;
  margin-left: 2.5%;
}
input {
  width: 50%;
  border-radius: 15px;
  padding: 5px;
  background-color: #efefef;
  margin-left: 25%;
}
<<<<<<< HEAD
.b-dropdown
{
height: 100px;
width: auto;

}
.b-dropdown-item
{margin-left: 0%;
overflow-y:scroll;
height: 10px;


}
.dropdown__menu
{
overflow-y:scroll;
height: 50px;
margin-left: 0%;
}

.btn-info{
background-color: #EF2942
=======
.b-dropdown {
  overflow-y: auto;
  height: auto;
}
.btn-info {
  background-color: #ef2942;
>>>>>>> 240cf2ed52c83809cda0060bda7def693d5b4b2a
}
</style>
