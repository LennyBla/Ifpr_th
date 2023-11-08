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
   Sidebar,
    Title,
  } from "../../components/common/index";

const AboutUsPage = () => {

    useEffect(() => {
        dispatch(fetchAsyncGenres());
       
      }, []);

    const dispatch = useDispatch();
    const games = useSelector(selectAllGames);
    const gamesStatus = useSelector(selectAllGamesStatus);
    const genres = useSelector(selectAllGenres);
    const genresStatus = useSelector(selectAllGenresStatus);
    return (
        <AboutUsPageWrapper>
            <div className='sc-aboutus section'>
               
                {genresStatus === STATUS.LOADING ? (
                <Preloader />
                ) : genres?.length > 0 ? (
                <Sidebar sliceValue={9} data={genres} />
                ) : (
                "No genres found!"
                )}
            </div>
        </AboutUsPageWrapper>
    )
}

export default AboutUsPage;

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