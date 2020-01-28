function bind_crtl_c_FactorialCalculation(){
    let isCtrl = false;

    document.onkeyup = function(e){ 
        if(e.which == 17) {
            isCtrl=false; 
        }
    }
    
    document.onkeydown = function(e){
    
        if(e.which == 17) {
            isCtrl=true;
        }
    
        if(e.which == 67 && isCtrl == true) {
            calculate_BMICalculation()
        }
    }
}