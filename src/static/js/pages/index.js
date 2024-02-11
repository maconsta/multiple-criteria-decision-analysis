/**
 * A procedure. Handles the logic for dynamically adding table rows in the criteria input table.  
 *
 * @return undefined;
 */
function addCriterion() {
    const lastTableRow = $("#js-criteria-table tr:last");

    // using string literal to make a multi-line string; regular string will also work, consider changing later for readability
    const newRow = `
    <tr class="draggable">
        <td>
            <input type="text" class="modern-input" placeholder="Add criterion name">
        </td>
        <td>
            <select name="beneficiality" class="modern-select" required>
                <option value="" selected disabled>Select type</option>
                <option value="max">Beneficial</option>
                <option value="min">Non-beneficial</option>
            </select>
        </td>
        <td class="edit"><div class="icon-container"><span class="reorder-icon reorder-icon--large" title="Reorder"></span><span class="x-icon x-icon--large remove-crit-btn" title="Remove"></span></div></td>
    </tr>`;

    lastTableRow.after(newRow);
    handleSorting();
}


/**
 * A procedure. Handles the logic for removing table rows in the criteria input table.  
 *
 * @return undefined;
 */
function removeCriterion(event) {
    if ($("#js-criteria-table tbody tr").length <= 1 || $(event.target).hasClass("x-icon--disabled")) {
        return;
    }

    $(event.target).closest("tr").remove();
    handleSorting();
}


/**
 * A procedure. Handles the logic for removing table rows in the alternatives input table.  
 *
 * @return undefined;
 */
function removeAlternative(event) {
    if ($("#js-alternatives-table tbody tr").length <= 1 || $(event.target).hasClass("x-icon--disabled")) {
        return;
    }

    $(event.target).closest("tr").remove();
}


/**
 * A procedure. Either enables or disables JqueryUI sorting in the criteria input table.  
 *
 * @return undefined;
 */
function handleSorting() {
    if ($("#js-criteria-table tbody tr").length <= 1) {
        $("#js-criteria-table tbody").sortable('disable');
    } else {
        $("#js-criteria-table tbody").sortable('enable');
    }
}


function constructAlternativesTable(event) {
    if ($("#js-alternatives-table tbody tr").length >= 1) {
        return;
    }

    const $tableRows = $("#js-criteria-table tbody tr");

    let error = false;
    let newHeader = "<tr><th class='align-center'>Name</th>";
    $tableRows.each(function () {
        const inputVal = $(this).find("input").val();
        const selectVal = $(this).find("select").val();

        if (inputVal == "" || selectVal == null) {
            error = true;
            return false;
        }

        newHeader += "<th class='align-center'>" + $(this).find("input").val() + "</th>";
    });
    newHeader += "<th class='edit align-center'>Edit</th></tr>";

    if (error) {
        alert("There are missing values in the criteria table. Please fix them before continuing.")
    } else {
        $("#js-alternatives-table thead").append(newHeader);
        addAlternative();
        disableCriteriaInput($("#js-criteria-table"));
    }
}


function constructWeightsTable(event) {
    if ($("#js-weights-table tbody tr").length >= 1) {
        return;
    }

    const isValid = validateCriteriaTable();
    if (!isValid) {
        alert("There are missing values in the criteria table. Please fix them before continuing.")
        return;
    }

    const $tableRows = $("#js-criteria-table tbody tr");
    const rowsCount = $tableRows.length;

    const selectHTML = `
        <select name="beneficiality" class="modern-select" required>
            <option value="" selected disabled>Select Value</option>
            <option value="1/9" data-reciprocal="9">1/9</option>
            <option value="1/8" data-reciprocal="8">1/8</option>
            <option value="1/7" data-reciprocal="7">1/7</option>
            <option value="1/6" data-reciprocal="6">1/6</option>
            <option value="1/5" data-reciprocal="5">1/5</option>
            <option value="1/4" data-reciprocal="4">1/4</option>
            <option value="1/3" data-reciprocal="3">1/3</option>
            <option value="1/2" data-reciprocal="2">1/2</option>
            <option value="1" data-reciprocal="1">1</option>
            <option value="2" data-reciprocal="1/2">2</option>
            <option value="3" data-reciprocal="1/3">3</option>
            <option value="4" data-reciprocal="1/4">4</option>
            <option value="5" data-reciprocal="1/5">5</option>
            <option value="6" data-reciprocal="1/6">6</option>
            <option value="7" data-reciprocal="1/7">7</option>
            <option value="8" data-reciprocal="1/8">8</option>
            <option value="9" data-reciprocal="1/9">9</option>
        </select>
    `;

    let newHeader = "<tr><th></th>";
    let newRows = "";
    $tableRows.each(function (i) {
        newHeader += "<th class='align-center'>" + $(this).find("input").val() + "</th>";

        newRows += "<tr><th class='align-center'>" + $(this).find("input").val() + "</th>";

        for (let j = 0; j < rowsCount; j++) {
            if (j == i) {
                newRows += "<td><select class='modern-select' disabled><option value='1' selected disabled>1</option></td>";
            } else {
                newRows += "<td>" + selectHTML.trim() + "</td>";
            }
        }
        newRows += "</tr>";
    });
    newHeader += "</tr>";

    $("#js-weights-table thead").append(newHeader);
    $("#js-weights-table tbody").append(newRows.trim());



    disableCriteriaInput($("#js-criteria-table"));

}


function addAlternative() {
    const $tableBody = $("#js-alternatives-table tbody");

    let newRow = "<tr><td><input type='text' class='modern-input' placeholder='Alternative Name'></td>";

    const $tableRows = $("#js-criteria-table tbody tr");
    $tableRows.each(function () {
        newRow += "<td><input type='number' class='modern-input' placeholder='Criterion value' step='any'></td>";
    });
    newRow += '<td class="edit"><div class="icon-container"><span class="x-icon x-icon--large remove-alt-btn" title="Remove"></span></div></td></tr>';

    $tableBody.append(newRow);
}


function accordionHandler(event) {
    const $chevron = $(event.currentTarget);
    if ($chevron.hasClass("chevron--disabled")) {
        return;
    }

    const className = $chevron.attr("data-for");
    $chevron.toggleClass("chevron--active");
    $(".accordion." + className).slideToggle();
}


function validateCriteriaTable() {
    let isValid = true;

    const $tableRows = $("#js-criteria-table tbody tr");
    $tableRows.each(function () {
        const inputVal = $(this).find("input").val();
        const selectVal = $(this).find("select").val();

        if (inputVal == "" || selectVal == null) {
            isValid = false;
            return false;
        }
    });

    return isValid;
}

function validateAlternativesTable() {
    let isValid = true;

    const $tableRows = $("#js-alternatives-table tbody tr");
    $tableRows.each(function () {
        const inputVal = $(this).find("input").val();

        if (inputVal == "") {
            isValid = false;
            return false;
        }
    });

    return isValid;
}


function updateChevronVisibility() {
    // const isValid = validateCriteriaTable();
    const isLocked = $("#js-criteria-table").hasClass("locked");

    $chevron = $(".accordion-header .chevron");
    if (isLocked) {
        $chevron.removeClass("chevron--disabled");
    } else {
        $chevron.addClass("chevron--disabled");
    }
}


function updateSetButtonVisibility() {
    const isValid = validateCriteriaTable();
    const isLocked = $("#js-criteria-table").hasClass("locked");

    const $btn = $("#js-set-criteria");
    if (isValid && !isLocked) {
        $btn.addClass("set-btn--active");
    } else {
        $btn.removeClass("set-btn--active");
    }
}


function disableCriteriaInput($table) {
    $("#js-criteria-table tbody").sortable('disable');
    $table.addClass("locked");
    $table.find(".modern-input").prop("disabled", true);
    $table.find(".modern-select").prop("disabled", true);
    $table.find(".reorder-icon").addClass("reorder-icon--disabled");
    $table.find(".x-icon").addClass("x-icon--disabled");
    $table.closest(".accordion").find(".add-btn").addClass("add-btn--disabled");
    $table.closest(".accordion").find(".unlock-btn").addClass("unlock-btn--active");
}


function enableCriteriaInput(event) {
    const $table = $(event.target).closest(".accordion").find("table");
    $(".chevron[data-for='alternatives'].chevron--active").click();
    $(".chevron[data-for='weights'].chevron--active").click();

    $table.removeClass("locked");
    $table.find("tbody").sortable('enable');
    $table.find(".modern-input").prop("disabled", false);
    $table.find(".modern-select").prop("disabled", false);
    $table.find(".reorder-icon").removeClass("reorder-icon--disabled");
    $table.find(".x-icon").removeClass("x-icon--disabled");
    $table.closest(".accordion").find(".add-btn").removeClass("add-btn--disabled");
    $table.closest(".accordion").find(".unlock-btn").removeClass("unlock-btn--active");

    $("#js-alternatives-table thead tr, #js-alternatives-table tbody tr ").remove();
    $("#js-weights-table thead tr, #js-weights-table tbody tr ").remove();
}


function closeAllAccordionsExcept(except) {
    $(".chevron").each(function () {
        if ($(this).hasClass("chevron--active") && $(this).is(except)) {
            $(thic).click();
        }
    });
}


function handleWeightInput(event) {
    // -1 because we need only the number of columns with input fields, thus removing the first col with the crit name
    const columnID = $(event.target).closest("td").index() - 1; 
    const rowID = $(event.target).closest("tr").index();

    const selectedVal = $(event.target).val();
    console.log($(event.target));
    const reciprocalVal = $(event.target).find(":selected").attr("data-reciprocal");
    
    const $row = $("#js-weights-table tbody tr").eq(columnID);
    const $select = $row.find("td").eq(rowID).find(".modern-select");
    // console.log(reciprocalVal);
    $select.val(reciprocalVal);
}


$(document).ready(function () {
    /* Adding event listeners */
    $("#js-add-criterion").on("click", addCriterion);
    $("#js-add-criterion").on("click", updateSetButtonVisibility);

    $("#js-add-alternative").on("click", addAlternative);

    $("#js-unlock-criteria").on("click", enableCriteriaInput);
    $("#js-unlock-criteria").on("click", updateSetButtonVisibility);
    $("#js-unlock-criteria").on("click", updateChevronVisibility);

    $(".accordion-header .chevron").on("click", accordionHandler);

    $("#js-criteria-table").on("change keyup", ".modern-input, .modern-select", updateSetButtonVisibility);

    $("#js-weights-table").on("change", ".modern-select", handleWeightInput);

    $("#js-set-criteria").on("click", constructWeightsTable);
    $("#js-set-criteria").on("click", constructAlternativesTable);
    $("#js-set-criteria").on("click", updateSetButtonVisibility);
    $("#js-set-criteria").on("click", updateChevronVisibility);


    $(document).on("click", ".remove-crit-btn", removeCriterion);
    $(document).on("click", ".remove-crit-btn", updateSetButtonVisibility);

    $(document).on("click", ".remove-alt-btn", removeAlternative);


    /* initialize sortable (JqueryUI) */
    $(".sortable").sortable({
        revert: "invalid",
        axis: "y",
        handle: ".reorder-icon",
        disabled: true
    });

});