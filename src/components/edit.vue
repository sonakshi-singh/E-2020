 <template >
  <div id="edit-container">
    <h1 style="font-size:60px;">Fill out Template</h1>
    
    <div>
            
     <label>Title</label>
      <b-form-input id="input-1" v-model="title" required placeholder="Enter title"></b-form-input>
      <label for="example-input">Choose a date</label>
      <b-form-datepicker id="example-datepicker" v-model="value" class="mb-2"></b-form-datepicker>
       <b-form-textarea id="textarea" v-model="text" placeholder="Enter something..." rows="3" max-rows="6"></b-form-textarea>
       <b-form-textarea id="textarea1" v-model="text1" placeholder="Enter something..." rows="3" max-rows="6"></b-form-textarea>


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
          'text1:''
         
         
        }
       
      }
    }
  


</script>

<style >

#input-1{

width: 50%;
margin-left: 25%;
margin-right:5%;
}
.b-form-datepicker
{
width: 50%;
margin-left: 25%;
margin-right:5%;

}

</style>



