import pytest
from unittest import mock
from src.controllers.usercontroller import UserController

@pytest.fixture
def mock_dao():
    return mock.MagicMock()

class TestGetUserByEmail:

    #These follwoing two functions could be parameterized I believe.
    def test_get_user_email_single_valid(self, mock_dao):
        #Arrange
        user_controller = UserController(mock_dao)
        print()
        #Act
        #Assert
        assert False == True
    
    def test_get_user_email_multiple_valid(self, mock_dao):
        #Arrange
        user_controller = UserController(mock_dao)
        print()
        #Act

        #Assert
        assert False == True
    

    def test_get_user_email_invalid_email(self, mock_dao):
        #Arrange

        user_controller = UserController(mock_dao)
        #Act
        #Assert
        with pytest.raises(ValueError):
            user_controller.get_user_by_email("invalid_email")
       
    
    def test_get_user_email_database_error(self, mock_dao):
        #Arrange
        #use of side_effect found in the unittest.mock documentation
        #"side_effect
        # This can either be a function to be called when the mock is called, an iterable or an exception (class or instance) to be raised.""
        mock_dao.find.side_effect = Exception("[Error] Database crached")
        user_controller = UserController(mock_dao)
        email = "valid.test@email.com"
        #Act
        #Assert
        with pytest.raises(Exception):
            user_controller.get_user_by_email(email)
        
    
  
    def test_get_user_email_no_user(self, mock_dao):
        """
            Function test behaviour of when there is no user for the given email.
            Expected result is None, as defined in the method doc text.
            Test fails because currently it always returns the first item when the length is not 1.
            I.e. raises an index error, instead of returning None.
        """
        #Arrange
        mock_dao.find.return_value = []
        user_controller = UserController(mock_dao)
        valid_email = "user.test@fakeuser.com"
        #Act
        res = user_controller.get_user_by_email(valid_email)
        #Assert
        assert res == None

    # #Show that could have parameterized the above 5 in 1 test case.
    # @pytest.mark.parametrize("", [

    # ])

    # def test_get_user_by_email_parameterized(self, mock_dao):
    #     #Arrange
    #     print()
    #     #Act

    #     #Assert
    #     assert False == True