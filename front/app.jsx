import React from "react";
import { useState } from 'react';
// import ReactDOM from "react-dom";
import { createRoot } from 'react-dom/client';

console.log("Hello World!");

const App = () => {
        const [requestInProgress, setRequestInProgress] = useState(false);
        const [sentImagePath, setSentImagePath] = useState(null);
        const [convertedImagePath, setConvertedImagePath] = useState(null);
        const onFileChange = (e) => {
                const formData = new FormData();
                formData.append('image', e.target.files[0]);
                setSentImagePath(URL.createObjectURL(e.target.files[0]));
                setRequestInProgress(true);
                fetch('/colorize', {
                        method: 'PUT',
                        credentials: 'same-origin',
                        body: formData
                })
                .then(resp => resp.blob())
                .then(blob => {
                        setRequestInProgress(false);
                        setConvertedImagePath(URL.createObjectURL(blob));
                })
        }

        return <div>
                <h1>Select an image:</h1>
                <input type="file" onChange={onFileChange} disabled={requestInProgress} />
                {sentImagePath &&
                        <>
                                <h1>Uploaded image:</h1>
                                <img src={sentImagePath} />
                                <h1>Resulting image:</h1>
                        </>}
                {requestInProgress &&
                        <p>Processing image...</p>}
                {convertedImagePath &&
                        <img src={convertedImagePath} />}
        </div>;
}

const container = document.getElementById('app');
const root = createRoot(container);
root.render(<App />);
// ReactDOM.render(<App />, document.getElementById("app"));