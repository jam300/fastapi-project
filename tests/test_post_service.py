import pytest
from unittest.mock import MagicMock
from app.schemas.post_schema import PostCreate
from app.services import post_service
from app.models.post_model import Post
from app.repositories import post_repository


@pytest.fixture
def fake_db():
    db = MagicMock()
    db.add.return_value = None
    db.commit.return_value = None
    db.refresh.return_value = None
    return db


@pytest.fixture
def fake_post_data():
    return PostCreate(
        title="Test title",
        content="Test content",
        published=True
    )


@pytest.fixture
def fake_user_id():
    return 1


def test_create_post_returns_post_instance(fake_db, fake_post_data, fake_user_id):
    # Arrange
    fake_post_instance = Post(
        id=1,
        title=fake_post_data.title,
        content=fake_post_data.content,
        published=fake_post_data.published,
        owner_id=fake_user_id
    )

    post_repository.create_post = MagicMock(return_value=fake_post_instance)

    # Act
    result = post_service.create_post(fake_post_data, fake_user_id, fake_db)

    # Assert
    assert isinstance(result, Post)
    assert result.title == fake_post_data.title
    assert result.content == fake_post_data.content
    assert result.published is True
    assert result.owner_id == fake_user_id
