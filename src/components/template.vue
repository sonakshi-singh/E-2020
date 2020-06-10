<template>
  <div>
   <h1 style="font-size:40px;margin-top:5%">View Template</h1>
    <b-container fluid="" class="template-container" >
      <br>
      <br><br><br><br><br><br><br><br><br><br>
           <input  :value="this.form.title" class = "title" placeholder ="text" >
          <b-row align-h="center">
            <b-col cols="4">
            <img :src="this.form.image1" class="ret"  >
            </b-col><b-col cols="4">
            <input  :value="this.form.text" class = "txt" placeholder ="text" @change="messageChange" >
            </b-col>
            </b-row >
          <b-row align-h="center">
            <b-col cols="4">
               <input  :value="this.form.text1" class = "txt" placeholder ="text" >
            </b-col><b-col cols="4">
              <img :src="this.form.image2" class="ret"  >
          </b-col></b-row>
          </b-container>
  </div>
</template>

<script>

export default {
    name:"Template",
    props: ["form"],
    data(){
        return {
            title: "title",
            images: [],
            messages: []
        }
    },
    methods: {
      messageChange(event){
        console.log(event)
        console.log(this.images)
      }
    }
};
</script>

<style lang="scss" scoped>
.template-container {
    padding-top: 100%;
    background-image: url("../assets/gradBackground.png");
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    min-height: 90%;
}
</style>
