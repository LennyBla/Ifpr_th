import { useState } from 'react';
import styled from 'styled-components';
import PropTypes from "prop-types";
import { AiOutlineMenu } from "react-icons/ai";
import { GenreItem } from '../genre';

const Tabs = ({ data }) => {
  const [activeTab, setActiveTab] = useState(data[0]); // using first genre as the default tab
  const [tabButtonStatus, setTabButtonStatus] = useState(false);

  const tabClickHandler = (id) => {
    data.map(item => {
      if(item.id === id){
        setActiveTab(item);
      }
    })
  }

  const tabButtonsHandler = () => setTabButtonStatus(prevStatus => !prevStatus);


  return (
    <TabsWrapper className='bg-white'>
      <div className='container'>
        <div className='tabs-content'>
            <div>
          <ul className={`tabs-buttons sidebar${tabButtonStatus ? "show" : ""}`}>
          <button type="button" className='tabs-buttons-close bg-white d-flex align-items-center justify-content-center' onClick={ tabButtonsHandler }>
              <AiOutlineMenu size = { 22 } />
            </button>
            {
              data.map(item => {
                return (
                  <li key = {item?.id} className={`tabs-button ${item?.id === activeTab.id ? 'tabs-active' : ""}`}>
                    <button className='sidebar text-white ' type="button" onClick={() => tabClickHandler(item?.id)}>{ item?.name }</button>
                  </li>
                )
              })
            }
          </ul>
          </div>
          <div className='tabs-body'>
            <div className='card-list'>
              {
                activeTab?.games?.map(item => (
                  <GenreItem key = {item.id} gameItem = { item } />
                ))
              }
            </div>
          </div>
        </div>
      </div>
    </TabsWrapper>
  )
}

export default Tabs;

Tabs.propTypes = {
  data: PropTypes.array,
  sliceValue: PropTypes.number
}

const TabsWrapper = styled.div`
  position: relative;
  min-height: 1000px;
  background-color: var(--clr-violet-dark-active);
 
  
  .tabs-buttons{
    
  
    /* box-shadow: rgba(0, 0, 0, 0.25) 0px 13px 27px -5px, rgba(0, 0, 0, 0.3) 0px 8px 16px -8px; */
    transition: var(--transition-default);

    

 

 
  }

  .tabs-button{
   float: left;
   list-style-type: none;
   margin: 0;
  padding: 0;
  margin: 0;
  padding: 0;
  
    button{

        
      padding: 12px 30px;
      font-family: 'Barlow';
      font-weight: 500;
      font-size: 18px;
      letter-spacing: 0.1em;
      /* border-bottom: 1px solid rgba(255, 255, 255, 0.03); */
      width: 100%;
      text-align: start;
    }

    &:hover:not(.tabs-active){
      background-color: rgba(0, 0, 0, 0.05);
    }
  }
  .tabs-active{
    background-color: var(--clr-pink-normal);
    button{
      color: var(--clr-white);
    }
  }

  .tabs-body{
    float: left;
    max-width: 1050px;
    min-width: 1025px;
    margin-left: 100px;
    margin-right: 100px;
  }
`;

    

