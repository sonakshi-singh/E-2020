 <template >
  <div id="edit-container">
    <h1 style="font-size:40px;margin-top:5%">Fill out Template</h1>
    
    <div>
            
    
      <b-form-input id="input-1" v-model="title" required placeholder="Enter title"></b-form-input>
      <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
       <b-form-textarea id="textarea" v-model="text" placeholder="What happened?" rows="3" max-rows="6"></b-form-textarea>
       <b-form-textarea id="textarea1" v-model="text1" placeholder="Top 3 things" rows="3" max-rows="6"></b-form-textarea>


      <b-button type="submit" variant="primary">Preview</b-button>
  




    </div>
  </div>
   
    
</template>

<script>
// import axios from "axios"
 export default {
   name:"edit",
    data() {
      return {
         
          'title':'',
          'name':'',
          'value':'',
          'text':'',
          'text1':''
         
         
        }
       
      }
    }
  


</script>

<style >

#input-1{

width: 50%;
margin-left: 25%;
margin-right:5%;
margin-bottom:2%;
}
.b-form-datepicker
{
width: 50%;
margin-left: 25%;
margin-right:5%;
padding-bottom:5%;

}
#textarea
{ 
  width:50%;
  margin-left:25%;
  margin-right:5%;
  margin-bottom:2%;
}
#textarea1
{
  width:50%;
  margin-left:25%;
  margin-right:5%;
  margin-bottom:2%;
}
</style>



