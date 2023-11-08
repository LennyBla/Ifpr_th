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

  
const SignUp = () => {

  

    return (
        <AboutUsPageWrapper>
            <div className='sc-aboutus section'>
                <div className='container'> 
                    <Title titleName={{
                        firstText: "Sign",
                        secondText: "Up"
                    }}/>
                </div>

               

            </div>
        </AboutUsPageWrapper>
    )
}

export default SignUp;

const AboutUsPageWrapper = styled.div`
background-color: var(--clr-violet-dark-active);
.sc-aboutus{
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

`