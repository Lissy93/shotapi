class MissingCloudinaryCredentialsError(ValueError):
    def __init__(self, missing_field):
        message = (
            f"{missing_field} is required when 'format' is 'cloudinary_url'"
        )
        super().__init__(message)
