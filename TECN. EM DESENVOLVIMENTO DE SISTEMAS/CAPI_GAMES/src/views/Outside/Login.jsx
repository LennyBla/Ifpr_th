import { useDispatch, useSelector } from 'react-redux';
import styled from 'styled-components';


import {
    selectAllGenres,
    selectAllGenresStatus,
  } from "../../redux/store/genreSlice";
  import {
    selectAllGames,
    selectAllGamesStatus,
  } from "../../redux/store/gameSlice";
  import { STATUS } from "../../utils/status";
  import { useEffect } from "react";
  import { fetchAsyncGenres } from "../../redux/utils/genreUtils";
  import {
    Preloader,
   
    Title,
  } from "../../components/common/index";



import { banner_image } from '../../utils/images';  

const Login = () => {

  

    return (
        <LoginUsPageWrapper style = {{
          background: `linear-gradient(0deg, rgba(0, 0, 0, 0.32), rgba(0, 0, 0, 0.32)), linear-gradient(248.75deg, rgba(0, 159, 157, 0.41) 0%, rgba(15, 10, 60, 0.41) 38.46%), url(${banner_image}) center/cover no-repeat`
        }}>
             <div className='sc-aboutus'>
                <div className='container'> 
                   
                   
               
                <section>
                  <p>
                    <input placeholder='email' className='input' type='email'/>
                    </p>
                    <p>
                    <input placeholder='senha' className='input' type='password'/>
                    </p>
                    <button type="button" className='banner-btn d-flex align-items-center'>     
                      <span className='btn-text text-green '>Login</span>
                    </button>
                   
                </section>
                </div>
                
            </div>
        </LoginUsPageWrapper>
    )
}

export default Login;

const LoginUsPageWrapper = styled.div`
background-color: var(--clr-violet-dark-active);
.sc-aboutus{
  display: flex;
    min-height: 100vh;
    padding-top: 65px;
}

.sc-popular {
    background-color: var(--clr-violet-dark-active);
    .section-btn {
      margin-top: 60px;
    }
  }

  .sc-join {
    min-height: 640px;

    .join-content {
      max-width: 600px;
    }

    .join-title {
      text-shadow: 0px 4px 4px 0px #00000040;
      font-size: 44px;
      letter-spacing: 0.09em;

      span {
        color: var(--clr-green-normal);
        font-family: var(--font-family-right);
      }
    }
  }

  .sc-genres {
    background-color: var(--clr-violet-dark-active);
  }

  .sc-stores {
    min-height: 841px;
  }
.button {
  background-color: #fff;
  width: 240px;
  height: 40px;
  border-radius: 40px;
  margin: 5px;
}

.banner-btn{
  min-width: 140px;
  width: 100%;
  height: 45px;
  padding-left: 38%;
  font-size: 16px;
  font-weight: 600;
  text-transform: uppercase;
  border: 2px solid var(--clr-green-normal);
  margin-top: 33px;


  .btn-icon{
    margin-right: 16px;
  }

  &:hover{
    background-color: var(--clr-green-normal);
    .btn-text{
      color: var(--clr-white);
      
    }
  }
}

.input {
  width: 280px;
  height: 40px;
  margin-bottom: 20px;
  border-radius: 3px;
  padding: 0 10px 0 10px;
}

`