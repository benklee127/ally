import React from 'react';
import { useModal } from '../../context/Modal';

function OpenModalButton({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  itemText,
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose // optional: callback function that will be called once the modal is closed
}) {
  const { setModalContent, setOnModalClose } = useModal();

  const onClick = () => {
    if (onModalClose) setOnModalClose(onModalClose);
    setModalContent(modalComponent);
    if (onButtonClick) onButtonClick();
  };
  
  if (buttonText) {
    return (
      <li>
        <button onClick={onClick}>{buttonText}</button>
      </li>
    )
  }
  else if (itemText) {
    return (
      <li onClick={onClick}>{itemText}</li>
    );
  }
}

export default OpenModalButton;
