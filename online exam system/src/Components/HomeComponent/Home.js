
 import style from "./Home.module.css";
 import pic2 from "../../images/2.png";
 import pic3 from "../../images/3.jpg";
 import axios from "axios";

 import {NavLink} from "react-router-dom";


    
    function Home(){
        const enableEyeTracking = async () => {
            try {
              await axios.post('http://localhost:5000/enable-eye-tracking');
              console.log('Eye tracking enabled successfully');
            } catch (error) {
              console.error('Error enabling eye tracking:', error.message);
            }
          };
          const enableSpeechDetection = async () => {
            try {
                await axios.post('http://localhost:5000/enable-speech-detector');
                console.log('Speech detection enabled successfully');
            } catch (error) {
                console.error('Error enabling speech detection:', error.message);
            }
        };
        return(
            <>
               <div id={style.header}>
                   <div id={style.headerHeadingBox}>
                        <h3>Vision Voice Navigator Exam System</h3> 
                    </div>
                </div>

              

              <div id={style.div2}>
            
                  <div className ={style.div3}>
                     <NavLink exact  to="/StudentLogin">
                        <img src={pic2} alt="" />
                        <span>Student</span>
                     </NavLink>
                  </div>

                  <div  className ={style.div3}>
                    <NavLink  to="/AdminLogin">
                       <img src={pic3} alt="" />
                       <span>Admin</span>
                     </NavLink> 
                  </div>
                  <div className={style.div4} >
                    <button className='active'  onClick={enableEyeTracking}>Enable Eye Tracking</button>
                    <button className='active'  onClick={enableSpeechDetection}>activate voice navigation</button>
                  </div>
                  
              </div>
              


             

            </>
        );
    }

     

    export default Home;