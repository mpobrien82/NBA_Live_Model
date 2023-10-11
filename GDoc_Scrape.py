<!DOCTYPE html>
<html>
<head>
    <title>NBA Live Model</title>
    <style>
        /* Your existing styles here */

        /* Add style for the upload button */
        #upload-button {
            padding: 10px 20px;
            background-color: #007bff; /* Blue color, you can change it */
            color: #fff;
            cursor: pointer;
        }

        /* Add styles for the input fields */
        .input-field {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NBA Live Model</h1>

        <!-- Add the upload button -->
        <input type="file" id="file-input" accept=".csv" style="display: none;">
        <label for="file-input" id="upload-button">Upload Projections</label>

        <!-- Input fields for game information -->
        <input type="text" class="input-field" placeholder="Game Score" id="game-score">
        <input type="text" class="input-field" placeholder="Game Time" id="game-time">

        <!-- Table for player stats -->
        <div class="scroll-container">
            <table id="player-table">
                <thead>
                    <tr>
                        <th>Team</th>
                        <th>Opponent</th>
                        <th>Player</th>
                        <th>Minutes</th>
                        <th>Points</th>
                        <th>Assists</th>
                        <th>Rebounds</th>
                        <th>Threes</th>
                    </tr>
                </thead>
                <!-- Data will be inserted here dynamically -->
            </table>
        </div>
    </div>

    <script>
        // Function to handle file input change
        document.querySelector('#file-input').addEventListener('change', handleFileUpload);

        function handleFileUpload(event) {
            const file = event.target.files[0];

            if (file) {
                // Handle the uploaded file, e.g., read and process the CSV data
                const reader = new FileReader();
                reader.onload = function(e) {
                    const csvData = e.target.result;

                    // Process the CSV data (parse and update the table)
                    processDataFromCSV(csvData);
                };
                reader.readAsText(file);
            }
        }

        // Function to process data from the uploaded CSV
        function processDataFromCSV(csvData) {
            // Parse and process the CSV data, then update the table
            const lines = csvData.split('\n');
            const playerTable = document.querySelector('#player-table');

            // Your code to process and update the table based on CSV data here
        }
    </script>
</body>
</html>

