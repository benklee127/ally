import React from 'react';
import { useModal } from '../../context/Modal';

export const OpenModalButton = ({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  buttonDiv,
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed
}) => {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };
  console.log(buttonDiv)
  return <div onClick={onClick} dangerouslySetInnerHTML={{__html: buttonDiv ? buttonDiv : buttonText}}></div>;
};

export default OpenModalButton;
