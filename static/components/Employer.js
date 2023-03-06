export default {        
  template: ` 

    <button :class="active ? 'text-red' : 'text-blue' " :disabled="processing"  @click="toggle"  > <slot/> </button> ` 
  ,

  props: {
    type: {
      type: String,
      default: 'primary'
    }
  },
  
  data (){
    return{
      processing: false ,
      active : 'false',
      assets : [],
      count: '0',
    };
  },

/* 
  created(){
    fetch('http://127.0.0.1:8000/employer/')
      .then(response=> response.json())

      .then( assets=>{ 
             console.log(assets);
             this.assets = assets;
             });

  }, */



  
  
  methods: {
    toggle (){

      fetch('http://127.0.0.1:8000/employer/')
        .then(response=> response.json())

        .then( assets=>{ 
              console.log(assets);
              this.assets = assets;
              });

              
      this.active = !this.active
      this.processing = !this.processing
      alert('Employee Successfully');
      this.buttonClass = 'text-blue'
      console.log('clicked')
      
    }      
}} 