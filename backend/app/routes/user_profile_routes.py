from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.db.models import User, session as sql_session
from backend.app import app


@app.route("/api/update-profile", methods=["POST"])
@jwt_required()
def update_profile():
    try:
        # Get the user ID from the JWT
        user_id = get_jwt_identity()
        user = sql_session.query(User).filter_by(user_id=user_id).first()
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 404

        # Get current and new emails from the request
        current_email = request.form.get("currentEmail")
        new_email = request.form.get("newEmail")

        if not current_email or not new_email:
            return (
                jsonify({"success": False, "message": "Email fields are required"}),
                400,
            )

        # Check if the current email matches the user's current email
        if user.email != current_email:
            return (
                jsonify({"success": False, "message": "Current email does not match"}),
                400,
            )

        # Check if the new email is the same as the current email
        if current_email == new_email:
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "New email cannot be the same as the current email",
                    }
                ),
                400,
            )

        # Check if the new email is already in use by another user
        existing_user = sql_session.query(User).filter_by(email=new_email).first()
        if existing_user and existing_user.user_id != user_id:
            return jsonify({"success": False, "message": "Email is already taken"}), 400

        # Update the email
        user.email = new_email
        sql_session.commit()
        return jsonify({"success": True, "message": "Email updated successfully!"})

    except Exception as e:
        print(f"Error updating profile: {e}")  # Log the error
        sql_session.rollback()
        return jsonify({"success": False, "message": "Failed to update profile"}), 500
