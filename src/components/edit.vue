 <template >
  <div id="edit-container">
    <h1 style="font-size:40px;margin-top:5%">Fill out Template</h1>
    
    <div>
            
    <b-form @submit="onSubmit" v-if="show" id="form">
      <b-form-input id="input-1" v-model="form.title" required placeholder="Enter title"></b-form-input>
      <b-form-datepicker id="example-datepicker" v-model="form.value" class="mb-2"></b-form-datepicker>
       <b-form-textarea id="textarea" v-model="form.text" placeholder="What happened?" rows="3" max-rows="6"></b-form-textarea>
       <b-form-textarea id="textarea1" v-model="form.text1" placeholder="Top 3 things" rows="3" max-rows="6"></b-form-textarea>

    </b-form>

    </div>
</div>
    
</template>
<script>
 export default {
   name:"edit",
   props: ['form'],
   data() {
      return {
        
      show: true
      }
    },
    methods: {
   onSubmit(evt) {
        evt.preventDefault()
        console.log(JSON.stringify(this.form));
        
        
        
        //console.log({title:this.title,value:this.value,text:this.text,text1:this.text1});
      },
 
/*function() {
	function toJSONString( form ) {
		var obj = {};
		var elements = form.querySelectorAll( "b-form-input,b-form-datepicker,b-form-textarea" );
		for( var i = 0; i < elements.length; ++i ) {
			var element = elements[i];
			var name = element.name;
			var value = element.value;
			if( name ) {
				obj[ name ] = value;
			}
		}
		return JSON.stringify( obj );
	}
	document.addEventListener( "DOMContentLoaded", function() {
		var form = document.getElementById( "test" );
		var output = document.getElementById( "output" );
		form.addEventListener( "onSubmit", function( e ) {
			e.preventDefault();
			var json = toJSONString( this );
			output.innerHTML = json;
		}, false);
  }); 
}
form_m(){
   var vm = this,
          formData= new FormData(vm.$refs.form)
      let jsonObject = {};
      for (const [key, value]  of formData.entries()) {
        jsonObject[key] = value;
      }
      console.log(jsonObject)
    }
    */
    }
 }
  
 
</script>
<style>
#input-1 {
  width: 50%;
  margin-left: 25%;
  margin-right: 5%;
  margin-bottom: 2%;
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
