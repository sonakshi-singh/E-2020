<template >
  <div id="edit-container">
    <!-- <div style="background-image: url(./src/body.jpg);"> -->
    <!-- <img alt="Vue logo" src="./body.jpg"> -->
    <h1 style="font-size:60px;">Fill out Template</h1>
    <div>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
     <label>Title</label>
      <b-form-group
        id="input-group-1"
        label="Title"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

<label for="example-input">Choose a date</label>
    <b-form-group id="input-group-2" label="Date" label-for="input-2">
      <b-form-input
        id="input-group-2"
        v-model="value"
        type="text"
        placeholder="YYYY-MM-DD"
        autocomplete="off"
      ></b-form-input>
      <b-form-group-append>
        <b-form-datepicker
          v-model="value"
          button-only
          right
          locale="en-US"
          aria-controls="example-input"
          @context="onContext"
        ></b-form-datepicker>
      </b-form-group-append>
    </b-form-group>


      <b-button type="submit" variant="primary">Submit</b-button>
  </b-form>




    </div>
   
    </div>
</template>

<script>
// import axios from "axios"
 export default {
   name:"edit",
    data() {
      return {
        form: {
          title: '',
          name:'',
          value:''
         
         
        },
       
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
       
        this.form.name = ''
        
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }


</script>

<style >
.ret{
    width: 300px;
    height :500px;
    padding:20px;
}

#edit-container { 
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
